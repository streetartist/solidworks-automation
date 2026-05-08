# DisplayWindowFromHandlex64 Method (IModelViewManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64`

Displays a .NET control in this model view on 64-bit machines.
Displays a .NET control in this model view on 64-bit machines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DisplayWindowFromHandlex64( _
   ByVal Name As System.String, _
   ByVal WindowHandle As System.Long, _
   ByVal SplitWindow As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelViewManager
Dim Name As System.String
Dim WindowHandle As System.Long
Dim SplitWindow As System.Boolean
Dim value As System.Boolean
 
value = instance.DisplayWindowFromHandlex64(Name, WindowHandle, SplitWindow)
```

```

System.bool DisplayWindowFromHandlex64( 
   System.string Name,
   System.long WindowHandle,
   System.bool SplitWindow
)
```

```

System.bool DisplayWindowFromHandlex64( 
   System.String^ Name,
   System.int64 WindowHandle,
   System.bool SplitWindow
) 
```

#### Parameters

*Name*
:   User-defined label that appears on the tab

*WindowHandle*
:   64-bit handle of the .NET control

*SplitWindow*
:   True to add a splitter window, false to not

#### Return Value

True if .NET control is created, false if not

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Example

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)  
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::CreateFeatureMgrWindowFromHandlex64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64.md)
