# SetDroppedFileFeatureName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileFeatureName`

Sets the name of the feature for the recently dropped file.
Sets the name of the feature for the recently dropped file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDroppedFileFeatureName( _
   ByVal FeatureName As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim FeatureName As System.String
Dim value As System.Boolean
 
value = instance.SetDroppedFileFeatureName(FeatureName)
```

```

System.bool SetDroppedFileFeatureName( 
   System.string FeatureName
)
```

```

System.bool SetDroppedFileFeatureName( 
   System.String^ FeatureName
) 
```

#### Parameters

*FeatureName*
:   Feature name

#### Return Value

True if the feature name is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetDroppedAtEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity.md)  
[IAssemblyDoc::SetDroppedFileConfigName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.md)  
[IAssemblyDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.md)
