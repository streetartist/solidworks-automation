# Width Property (ILayer)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Width`

Gets and sets the line width for this layer.
Gets and sets the line width for this layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Width As System.Integer
```

```

Dim instance As ILayer
Dim value As System.Integer
 
instance.Width = value
 
value = instance.Width
```

```

System.int Width {get; set;}
```

```

property System.int Width {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Line width as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Example

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)  
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)  
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.md)  
[ILayer::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Style.md)
