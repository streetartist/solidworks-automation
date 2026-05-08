# ExplodeDistance Property (IPartExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~ExplodeDistance`

Gets or sets the distance to move bodies in this explode step.
Gets or sets the distance to move bodies in this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExplodeDistance As System.Double
```

```

Dim instance As IPartExplodeStep
Dim value As System.Double
 
instance.ExplodeDistance = value
 
value = instance.ExplodeDistance
```

```

System.double ExplodeDistance {get; set;}
```

```

property System.double ExplodeDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance in meters to move bodies

Example

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)  
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.md)
