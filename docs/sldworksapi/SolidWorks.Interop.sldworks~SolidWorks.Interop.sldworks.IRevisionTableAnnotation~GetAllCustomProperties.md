# GetAllCustomProperties Method (IRevisionTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties`

Gets a list of available custom properties that can be used for a custom properties column in this revision table annotation.
Gets a list of available custom properties that can be used for a custom properties column in this revision table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllCustomProperties() As System.Object
```

```

Dim instance As IRevisionTableAnnotation
Dim value As System.Object
 
value = instance.GetAllCustomProperties()
```

```

System.object GetAllCustomProperties()
```

```

System.Object^ GetAllCustomProperties(); 
```

#### Return Value

Array of strings of available custom properties

Remarks

This method only works for SOLIDWORKS documents created or saved in SOLIDWORKS 2005 or later.

The list of available custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty.md)  
[IRevisionTableAnnotation::IGetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.md)  
[IRevisionTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.md)  
[IRevisionTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.md)
