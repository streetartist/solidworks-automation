# Style Property (ILayer)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Style`

Gets and sets the line style for this layer.
Gets and sets the line style for this layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Style As System.Integer
```

```

Dim instance As ILayer
Dim value As System.Integer
 
instance.Style = value
 
value = instance.Style
```

```

System.int Style {get; set;}
```

```

property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

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
[ILayer::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Width.md)
