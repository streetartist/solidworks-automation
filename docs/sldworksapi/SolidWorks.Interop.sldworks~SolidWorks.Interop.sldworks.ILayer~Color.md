# Color Property (ILayer)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Color`

Gets and sets the line color for this layer.
Gets and sets the line color for this layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Color As System.Integer
```

```

Dim instance As ILayer
Dim value As System.Integer
 
instance.Color = value
 
value = instance.Color
```

```

System.int Color {get; set;}
```

```

property System.int Color {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

COLORREF value for the color

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
