# SolidBodies Property (IMirrorPartFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SolidBodies`

Gets or sets whether to import solid bodies.
Gets or sets whether to import solid bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolidBodies As System.Boolean
```

```

Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean
 
instance.SolidBodies = value
 
value = instance.SolidBodies
```

```

System.bool SolidBodies {get; set;}
```

```

property System.bool SolidBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import solid bodies, false to not

Example

See the [IMirrorPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md)  
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.md)
