# GetImportedFileName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFileName`

Gets the file name from an imported feature.
Gets the file name from an imported feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetImportedFileName() As System.String
```

```

Dim instance As IFeature
Dim value As System.String
 
value = instance.GetImportedFileName()
```

```

System.string GetImportedFileName()
```

```

System.String^ GetImportedFileName(); 
```

#### Return Value

File name of the imported feature

Remarks

This method applies only to imported features. All other features return an empty string. To get the type of this feature, use [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::SetImportedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFileName.md)
