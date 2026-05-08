# Visible Property (ILayer)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Visible`

Gets or sets the visibility of this layer.
Gets or sets the visibility of this layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Boolean
```

```

Dim instance As ILayer
Dim value As System.Boolean
 
instance.Visible = value
 
value = instance.Visible
```

```

System.bool Visible {get; set;}
```

```

property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the layer is visible, false if the layer is not visible (see **Remarks**)

Remarks

After setting this property to the opposite state, call [ILayer::Printable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Printable.md) to check its state, because setting ILayer::Visible might change the state of ILayer::Printable.

To ensure that ILayer::Visible and ILayer::Printable are set to the desired states, perform the following steps in this order:

1. Set ILayer::Visible.
2. Get the state of ILayer::Printable.
3. Set ILayer::Printable if necessary.

Example

[Determine if Layer is Visible (VBA)](Determine_if_Layer_is_Visible_Example_VB.htm)  
[Get Layers (C#)](Get_Layers_Example_CSharp.htm)  
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)  
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.md)
