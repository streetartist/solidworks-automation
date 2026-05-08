# ExplodeDistance Property (IExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeDistance`

Gets or sets the distance to move components in this regular or radial explode step.
Gets or sets the distance to move components in this regular or radial explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExplodeDistance As System.Double
```

```

Dim instance As IExplodeStep
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

Distance in meters to move components

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
