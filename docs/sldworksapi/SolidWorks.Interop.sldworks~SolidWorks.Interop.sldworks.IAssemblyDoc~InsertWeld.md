# InsertWeld Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertWeld`

Obsolete. Do not use. Superseded by IFeatureManager::InsertCosmeticWeldBead.
Obsolete. Do not use. Superseded by [IFeatureManager::InsertCosmeticWeldBead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertWeld( _
   ByVal Type As System.String, _
   ByVal Shape As System.String, _
   ByVal TopDelta As System.Double, _
   ByVal BottomDelta As System.Double, _
   ByVal Radius As System.Double, _
   ByVal Part As System.String _
) 
```

```

Dim instance As IAssemblyDoc
Dim Type As System.String
Dim Shape As System.String
Dim TopDelta As System.Double
Dim BottomDelta As System.Double
Dim Radius As System.Double
Dim Part As System.String
 
instance.InsertWeld(Type, Shape, TopDelta, BottomDelta, Radius, Part)
```

```

void InsertWeld( 
   System.string Type,
   System.string Shape,
   System.double TopDelta,
   System.double BottomDelta,
   System.double Radius,
   System.string Part
)
```

```

void InsertWeld( 
   System.String^ Type,
   System.String^ Shape,
   System.double TopDelta,
   System.double BottomDelta,
   System.double Radius,
   System.String^ Part
) 
```

#### Parameters

*Type*
:   Weld bead type

*Shape*
:   Surface shape

*TopDelta*
:   Distance for the top surface delta, if appropriate

*BottomDelta*
:   Distance for the bottom surface delta, if appropriate

*Radius*
:   Weld radius, if appropriate

*Part*
:   Path and filename for the part used for the weld; this file is created and merged into your assembly

Remarks

For the most up-to-date list of available types and shapes, see **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english\gtol.sym**.

To programmatically select the top, stop, and contact faces for the weld bead and pass them as arrays, use [IAssemblyDoc::InsertWeld2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertWeld2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.md)  
[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)
