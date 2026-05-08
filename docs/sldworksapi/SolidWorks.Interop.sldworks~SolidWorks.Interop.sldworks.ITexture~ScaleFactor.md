# ScaleFactor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~ScaleFactor`

Gets or sets the granularity of the texture.
Gets or sets the granularity of the texture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleFactor As System.Double
```

```

Dim instance As ITexture
Dim value As System.Double
 
instance.ScaleFactor = value
 
value = instance.ScaleFactor
```

```

System.double ScaleFactor {get; set;}
```

```

property System.double ScaleFactor {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.001 < Granularity of the texture < 1000000.00

Example

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)  
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.md)
