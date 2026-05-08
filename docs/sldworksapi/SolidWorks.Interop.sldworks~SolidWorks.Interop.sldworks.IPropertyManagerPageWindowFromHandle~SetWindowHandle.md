# SetWindowHandle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandle`

Sets the handle of this .NET control.
Sets the handle of this .NET control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetWindowHandle( _
   ByVal WindowHandle As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageWindowFromHandle
Dim WindowHandle As System.Integer
Dim value As System.Boolean
 
value = instance.SetWindowHandle(WindowHandle)
```

```

System.bool SetWindowHandle( 
   System.int WindowHandle
)
```

```

System.bool SetWindowHandle( 
   System.int WindowHandle
) 
```

#### Parameters

*WindowHandle*
:   Handle of the .NET control

#### Return Value

True if handle is set, false if not

Remarks

If your application must be x64 compatible, then use [IPropertyManagerPageWindowFromHandle::SetWindowHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandlex64.md).

You must call this method to initialize the .NET control handle whenever you call [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md), because .NET control handles are destroyed with their forms when the PropertyManager page closes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.md)  
[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.md)
