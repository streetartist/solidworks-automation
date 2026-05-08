# RayIntersections Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~RayIntersections`

Obsolete. Superseded by IModelDoc2::RayIntersections.
Obsolete. Superseded by [IModelDoc2::RayIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RayIntersections( _
   ByVal BodiesIn As System.Object, _
   ByVal BasePointsIn As System.Object, _
   ByVal VectorsIn As System.Object, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim BodiesIn As System.Object
Dim BasePointsIn As System.Object
Dim VectorsIn As System.Object
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim value As System.Integer
 
value = instance.RayIntersections(BodiesIn, BasePointsIn, VectorsIn, Options, HitRadius, Offset)
```

```

System.int RayIntersections( 
   System.object BodiesIn,
   System.object BasePointsIn,
   System.object VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

```

System.int RayIntersections( 
   System.Object^ BodiesIn,
   System.Object^ BasePointsIn,
   System.Object^ VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset
) 
```

#### Parameters

*BodiesIn*

*BasePointsIn*

*VectorsIn*

*Options*

*HitRadius*

*Offset*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
