# IRayIntersections Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IRayIntersections`

Obsolete. Superseded by IModelDoc2::IRayIntersections.
Obsolete. Superseded by [IModelDoc2::IRayIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRayIntersections.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRayIntersections( _
   ByRef BodiesIn As Body, _
   ByVal NumBodies As System.Integer, _
   ByRef BasePointsIn As System.Double, _
   ByRef VectorsIn As System.Double, _
   ByVal NumRays As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim BodiesIn As Body
Dim NumBodies As System.Integer
Dim BasePointsIn As System.Double
Dim VectorsIn As System.Double
Dim NumRays As System.Integer
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim value As System.Integer
 
value = instance.IRayIntersections(BodiesIn, NumBodies, BasePointsIn, VectorsIn, NumRays, Options, HitRadius, Offset)
```

```

System.int IRayIntersections( 
   ref Body BodiesIn,
   System.int NumBodies,
   ref System.double BasePointsIn,
   ref System.double VectorsIn,
   System.int NumRays,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

```

System.int IRayIntersections( 
   Body^% BodiesIn,
   System.int NumBodies,
   System.double% BasePointsIn,
   System.double% VectorsIn,
   System.int NumRays,
   System.int Options,
   System.double HitRadius,
   System.double Offset
) 
```

#### Parameters

*BodiesIn*

*NumBodies*

*BasePointsIn*

*VectorsIn*

*NumRays*

*Options*

*HitRadius*

*Offset*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
