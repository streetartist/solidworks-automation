# DisplayWindowFromHandle Method (IModelViewManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandle`

Displays a .NET control in this model view.
Displays a .NET control in this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DisplayWindowFromHandle( _
   ByVal Name As System.String, _
   ByVal WindowHandle As System.Integer, _
   ByVal SplitWindow As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelViewManager
Dim Name As System.String
Dim WindowHandle As System.Integer
Dim SplitWindow As System.Boolean
Dim value As System.Boolean
 
value = instance.DisplayWindowFromHandle(Name, WindowHandle, SplitWindow)
```

```

System.bool DisplayWindowFromHandle( 
   System.string Name,
   System.int WindowHandle,
   System.bool SplitWindow
)
```

```

System.bool DisplayWindowFromHandle( 
   System.String^ Name,
   System.int WindowHandle,
   System.bool SplitWindow
) 
```

#### Parameters

*Name*
:   User-defined label that appears on the tab

*WindowHandle*
:   Handle of the .NET control

*SplitWindow*
:   True to add a splitter window, false to not

#### Return Value

True if .NET control is created, false if not

Remarks

If your application must be x64 compatible, then use [IModelViewManager::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateFeatureMgrWindowFromHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle.md)
