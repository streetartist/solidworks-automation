# SaveAsText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText`

Obsolete. Superseded by ITableAnnotation::SaveAsText2.
Obsolete. Superseded by [ITableAnnotation::SaveAsText2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAsText( _
   ByVal FileName As System.String, _
   ByVal Separator As System.String _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim FileName As System.String
Dim Separator As System.String
Dim value As System.Boolean
 
value = instance.SaveAsText(FileName, Separator)
```

```

System.bool SaveAsText( 
   System.string FileName,
   System.string Separator
)
```

```

System.bool SaveAsText( 
   System.String^ FileName,
   System.String^ Separator
) 
```

#### Parameters

*FileName*
:   Full path and filename of text data file (see **Remarks**)

*Separator*
:   Character or string to use to separate each of the text within each of the cells in the table in the text file

#### Return Value

True if table is saved as a text file, false if not

Remarks

You must specify a filename. It should include the path, filename, and filename extension to which to save the table as a text file.

|  |  |
| --- | --- |
| **If a file of the specified name in the specified path...** | **Then it is...** |
| Exists | Overwritten |
| Does not exist | Created |

The Separator argument is typically a single character, but it can be a string. If Separator is empty, then the tab character is used.

**NOTE**: Although you can save a table as a text file for use with other applications like Microsoft Excel, you cannot currently import a text file to a table in SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SaveAsPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsPDF.md)  
[ITableAnnotation::SaveAsTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsTemplate.md)
