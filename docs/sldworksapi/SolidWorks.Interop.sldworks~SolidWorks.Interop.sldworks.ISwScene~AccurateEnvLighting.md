# AccurateEnvLighting Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AccurateEnvLighting`

Gets or sets whether to use the accurate environment lighting calculations from the high dynamic range imaging (HDRI) scene environment.
Gets or sets whether to use the accurate environment lighting calculations from the high dynamic range imaging (HDRI) scene environment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AccurateEnvLighting As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.AccurateEnvLighting = value
 
value = instance.AccurateEnvLighting
```

```

System.bool AccurateEnvLighting {get; set;}
```

```

property System.bool AccurateEnvLighting {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the accurate environment lighting calculations from the HDRI scene environment, false to not

Remarks

This property is valid only when a ray-trace rendering engine is active.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
