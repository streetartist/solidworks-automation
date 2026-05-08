# Height Property (IPropertyManagerPageWindowFromHandle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~Height`

Gets or sets the height of this .NET control.
Gets or sets the height of this .NET control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Height As System.Integer
```

```

Dim instance As IPropertyManagerPageWindowFromHandle
Dim value As System.Integer
 
instance.Height = value
 
value = instance.Height
```

```

System.int Height {get; set;}
```

```

property System.int Height {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Height of the control

Remarks

This property only applies to some .NET controls.

The height is in dialog-box units. You can convert these values to screen units (pixels) by using the Windows MapDialogRect function.

Example

See the [IPropertyManagerPageWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.md)  
[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.md)
