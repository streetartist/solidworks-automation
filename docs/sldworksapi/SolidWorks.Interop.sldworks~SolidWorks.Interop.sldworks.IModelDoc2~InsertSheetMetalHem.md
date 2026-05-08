# InsertSheetMetalHem Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalHem`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalHem.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalHem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSheetMetalHem( _
   ByVal Type As System.Integer, _
   ByVal Position As System.Integer, _
   ByVal Reverse As System.Boolean, _
   ByVal DLength As System.Double, _
   ByVal DGap As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal DRad As System.Double, _
   ByVal DMiterGap As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Type As System.Integer
Dim Position As System.Integer
Dim Reverse As System.Boolean
Dim DLength As System.Double
Dim DGap As System.Double
Dim DAngle As System.Double
Dim DRad As System.Double
Dim DMiterGap As System.Double
 
instance.InsertSheetMetalHem(Type, Position, Reverse, DLength, DGap, DAngle, DRad, DMiterGap)
```

```

void InsertSheetMetalHem( 
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap
)
```

```

void InsertSheetMetalHem( 
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap
) 
```

#### Parameters

*Type*

*Position*

*Reverse*

*DLength*

*DGap*

*DAngle*

*DRad*

*DMiterGap*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
