# CreateFeatureMgrView Method (IModelViewManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView`

Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2.
Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrView( _
   ByVal PPicture As System.Object, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim PPicture As System.Object
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrView(PPicture, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrView( 
   System.object PPicture,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrView( 
   System.Object^ PPicture,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*PPicture*

*ToolTip*

*WhichPane*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)
