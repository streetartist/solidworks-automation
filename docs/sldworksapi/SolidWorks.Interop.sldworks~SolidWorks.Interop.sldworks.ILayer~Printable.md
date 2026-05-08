# Printable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Printable`

Gets and sets whether this layer is printed when the drawing document is printed.
Gets and sets whether this layer is printed when the drawing document is printed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Printable As System.Boolean
```

```

Dim instance As ILayer
Dim value As System.Boolean
 
instance.Printable = value
 
value = instance.Printable
```

```

System.bool Printable {get; set;}
```

```

property System.bool Printable {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the layer is printable, false if the layer is not visible (see **Remarks**)

Remarks

Always call this property after setting [ILayer::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Visible.md) to the opposite state, because setting ILayer::Visible might change the state of ILayer::Printable. It is not possible to make a layer printable if it is not visible.

To ensure that ILayer::Visible and ILayer::Printable are set to the desired states, perform the following steps in this order:

1. Set ILayer::Visible.
2. Get the state of ILayer::Printable.
3. Set ILayer::Printable if necessary.

Example

See the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.md)
