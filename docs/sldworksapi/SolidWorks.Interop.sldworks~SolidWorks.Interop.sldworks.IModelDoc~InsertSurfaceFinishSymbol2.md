# InsertSurfaceFinishSymbol2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertSurfaceFinishSymbol2`

Obsolete. Superseded by IModelDoc2::InsertSurfaceFinishSymbol2.
Obsolete. Superseded by [IModelDoc2::InsertSurfaceFinishSymbol2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSurfaceFinishSymbol2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSurfaceFinishSymbol2( _
   ByVal SymType As System.Integer, _
   ByVal LeaderType As System.Integer, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double, _
   ByVal LaySymbol As System.Integer, _
   ByVal ArrowType As System.Integer, _
   ByVal MachAllowance As System.String, _
   ByVal OtherVals As System.String, _
   ByVal ProdMethod As System.String, _
   ByVal SampleLen As System.String, _
   ByVal MaxRoughness As System.String, _
   ByVal MinRoughness As System.String, _
   ByVal RoughnessSpacing As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim SymType As System.Integer
Dim LeaderType As System.Integer
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim LaySymbol As System.Integer
Dim ArrowType As System.Integer
Dim MachAllowance As System.String
Dim OtherVals As System.String
Dim ProdMethod As System.String
Dim SampleLen As System.String
Dim MaxRoughness As System.String
Dim MinRoughness As System.String
Dim RoughnessSpacing As System.String
Dim value As System.Boolean
 
value = instance.InsertSurfaceFinishSymbol2(SymType, LeaderType, LocX, LocY, LocZ, LaySymbol, ArrowType, MachAllowance, OtherVals, ProdMethod, SampleLen, MaxRoughness, MinRoughness, RoughnessSpacing)
```

```

System.bool InsertSurfaceFinishSymbol2( 
   System.int SymType,
   System.int LeaderType,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.int LaySymbol,
   System.int ArrowType,
   System.string MachAllowance,
   System.string OtherVals,
   System.string ProdMethod,
   System.string SampleLen,
   System.string MaxRoughness,
   System.string MinRoughness,
   System.string RoughnessSpacing
)
```

```

System.bool InsertSurfaceFinishSymbol2( 
   System.int SymType,
   System.int LeaderType,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.int LaySymbol,
   System.int ArrowType,
   System.String^ MachAllowance,
   System.String^ OtherVals,
   System.String^ ProdMethod,
   System.String^ SampleLen,
   System.String^ MaxRoughness,
   System.String^ MinRoughness,
   System.String^ RoughnessSpacing
) 
```

#### Parameters

*SymType*

*LeaderType*

*LocX*

*LocY*

*LocZ*

*LaySymbol*

*ArrowType*

*MachAllowance*

*OtherVals*

*ProdMethod*

*SampleLen*

*MaxRoughness*

*MinRoughness*

*RoughnessSpacing*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
