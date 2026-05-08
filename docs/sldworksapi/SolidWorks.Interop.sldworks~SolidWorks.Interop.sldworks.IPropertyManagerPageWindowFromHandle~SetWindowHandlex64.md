# SetWindowHandlex64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandlex64`

Sets the handle of this .NET control on 64-bit machines.
Sets the handle of this .NET control on 64-bit machines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetWindowHandlex64( _
   ByVal WindowHandle As System.Long _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageWindowFromHandle
Dim WindowHandle As System.Long
Dim value As System.Boolean
 
value = instance.SetWindowHandlex64(WindowHandle)
```

```

System.bool SetWindowHandlex64( 
   System.long WindowHandle
)
```

```

System.bool SetWindowHandlex64( 
   System.int64 WindowHandle
) 
```

#### Parameters

*WindowHandle*
:   64-bit handle of the .NET control

#### Return Value

True if handle is set, false if not

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

You must call this method to initialize the .NET control handle whenever you call [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md), because .NET control handles are destroyed with their forms when the PropertyManager page closes.

Example

See the [IPropertyManagerPageWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.md)  
[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.md)
