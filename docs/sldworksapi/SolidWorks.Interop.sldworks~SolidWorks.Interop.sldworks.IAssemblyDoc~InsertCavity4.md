# InsertCavity4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertCavity4`

Inserts a cavity to the active part using a selected component.
Inserts a cavity to the active part using a selected component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertCavity4( _
   ByVal ScaleFactor_x As System.Double, _
   ByVal ScaleFactor_y As System.Double, _
   ByVal ScaleFactor_z As System.Double, _
   ByVal IsUniform As System.Boolean, _
   ByVal ScaleType As System.Integer, _
   ByVal KeepPieceIndex As System.Integer _
) 
```

```

Dim instance As IAssemblyDoc
Dim ScaleFactor_x As System.Double
Dim ScaleFactor_y As System.Double
Dim ScaleFactor_z As System.Double
Dim IsUniform As System.Boolean
Dim ScaleType As System.Integer
Dim KeepPieceIndex As System.Integer
 
instance.InsertCavity4(ScaleFactor_x, ScaleFactor_y, ScaleFactor_z, IsUniform, ScaleType, KeepPieceIndex)
```

```

void InsertCavity4( 
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType,
   System.int KeepPieceIndex
)
```

```

void InsertCavity4( 
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType,
   System.int KeepPieceIndex
) 
```

#### Parameters

*ScaleFactor\_x*
:   Scaling factor in the x direction

*ScaleFactor\_y*
:   Scaling factor in the y direction

*ScaleFactor\_z*
:   Scaling factor in the z direction

*IsUniform*
:   True to use the first scale argument as the uniform scale, false to not

*ScaleType*
:   Type of scaling as defined in [swCavityScaleType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCavityScaleType_e.html)

*KeepPieceIndex*
:   Piece to keep if there is ambiguity

Remarks

This operation is performed in the context of an assembly document. The component being edited in the context of the assembly receives the new cavity feature.

Set the scaleFactor argument as appropriate for your casting material. The scaling factor is expressed as a percentage (+/- 20%) of the size of the cavity part. Pass it in as a value within the range of -20 to +20.

SOLIDWORKS uses the following formula to determine the size of the cavity:

cavitysize = partsize \* (1 + scaleFactor/100)

When there is ambiguity in the result of a cut, SOLIDWORKS uses KeepPieceIndex to determine which result to use. You can set this parameter to -1 if there is no ambiguity; otherwise, you should use the index of the result, in the range between 0 and 1 less than the possible number of outcomes.

Example

[Insert Cavity (C#)](Insert_Cavity_Example_CSharp.htm)  
[Insert Cavity (VB.NET)](Insert_Cavity_Example_VBNET.htm)  
[Insert Cavity (VBA)](Insert_Cavity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)
