# FeatureFillet3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureFillet3`

Obsolete. Superseded by IModelDoc2::FeatureFillet3.
Obsolete. Superseded by [IModelDoc2::FeatureFillet3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureFillet3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureFillet3( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal Ftyp As System.Integer, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal UseHelpPoint As System.Boolean, _
   ByVal UseTangentHoldLine As System.Boolean _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim R1 As System.Double
Dim Propagate As System.Boolean
Dim Ftyp As System.Integer
Dim VarRadTyp As System.Boolean
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Object
Dim UseHelpPoint As System.Boolean
Dim UseTangentHoldLine As System.Boolean
Dim value As System.Integer
 
value = instance.FeatureFillet3(R1, Propagate, Ftyp, VarRadTyp, OverflowType, NRadii, Radii, UseHelpPoint, UseTangentHoldLine)
```

```

System.int FeatureFillet3( 
   System.double R1,
   System.bool Propagate,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.object Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine
)
```

```

System.int FeatureFillet3( 
   System.double R1,
   System.bool Propagate,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.Object^ Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine
) 
```

#### Parameters

*R1*

*Propagate*

*Ftyp*

*VarRadTyp*

*OverflowType*

*NRadii*

*Radii*

*UseHelpPoint*

*UseTangentHoldLine*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
