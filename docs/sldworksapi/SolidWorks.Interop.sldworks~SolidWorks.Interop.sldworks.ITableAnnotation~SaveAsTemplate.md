# SaveAsTemplate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsTemplate`

Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same.
Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAsTemplate( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SaveAsTemplate(FileName)
```

```

System.bool SaveAsTemplate( 
   System.string FileName
)
```

```

System.bool SaveAsTemplate( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Full path and filename to which to save the table template file (see **Remarks**)

#### Return Value

True if the table is saved as a template file, false if not

Remarks

You must specify a filename. It should include the path, filename, and filename extension to which to save the table as a template file.

|  |  |
| --- | --- |
| **If a file of the specified name in the specified path...** | **Then it is...** |
| Exists | Overwritten |
| Does not exist | Created |

The filename extension of the file does not matter, but to be consistent with the SOLIDWORKS naming conventions, the following extensions should be used:

- .**sldbomtbt** for BOM tables
- .**sldrevtbt** for revision tables
- .**sldholtbt** for hole tables
- .**sldtbt** for general tables

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SaveAsPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsPDF.md)  
[ITableAnnotation::SaveAsText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText.md)
