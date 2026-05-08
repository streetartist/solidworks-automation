# SetImportedFileName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFileName`

Sets the file name of an imported feature.
Sets the file name of an imported feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetImportedFileName( _
   ByVal ImpName As System.String _
) As System.Boolean
```

```

Dim instance As IFeature
Dim ImpName As System.String
Dim value As System.Boolean
 
value = instance.SetImportedFileName(ImpName)
```

```

System.bool SetImportedFileName( 
   System.string ImpName
)
```

```

System.bool SetImportedFileName( 
   System.String^ ImpName
) 
```

#### Parameters

*ImpName*
:   New filename of the imported feature

#### Return Value

True if the filename was changed, false if not

Remarks

This method applies only to imported features. To get the type of this feature, use [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetImportedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFileName.md)
