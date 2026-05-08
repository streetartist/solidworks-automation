# Entity Property (IEdgePoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~Entity`

Gets or sets edge or reference curve on which the point is located.
Gets or sets edge or reference curve on which the point is located.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Entity As System.Object
```

```

Dim instance As IEdgePoint
Dim value As System.Object
 
instance.Entity = value
 
value = instance.Entity
```

```

System.object Entity {get; set;}
```

```

property System.Object^ Entity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [reference curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.md)  
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.md)
