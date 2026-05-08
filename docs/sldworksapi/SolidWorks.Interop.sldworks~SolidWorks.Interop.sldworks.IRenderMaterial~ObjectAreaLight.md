# ObjectAreaLight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ObjectAreaLight`

Gets or sets whether the appearance is an object area light or whether it has realistic falloff, or both.
Gets or sets whether the appearance is an object area light or whether it has realistic falloff, or both.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ObjectAreaLight As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.ObjectAreaLight = value
 
value = instance.ObjectAreaLight
```

```

System.int ObjectAreaLight {get; set;}
```

```

property System.int ObjectAreaLight {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

True if the appearance has an object area light or it has realistic falloff, or both; false if it does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
