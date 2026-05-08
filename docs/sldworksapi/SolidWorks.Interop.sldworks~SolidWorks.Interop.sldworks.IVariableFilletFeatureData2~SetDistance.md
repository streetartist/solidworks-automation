# SetDistance Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetDistance`

Sets the Distance 2 radius for this asymmetric fillet.
Sets the Distance 2 radius for this asymmetric fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDistance( _
   ByVal PFilletItem As System.Object, _
   ByVal Dist2 As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim Dist2 As System.Double
 
instance.SetDistance(PFilletItem, Dist2)
```

```

void SetDistance( 
   System.object PFilletItem,
   System.double Dist2
)
```

```

void SetDistance( 
   System.Object^ PFilletItem,
   System.double Dist2
) 
```

#### Parameters

*PFilletItem*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) at which to set the Distance 2 radius

*Dist2*
:   Distance 2 radius at the vertex specified by PFilletItem

Remarks

Call [IVariableFilletFeatureData2::SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.md) to set the Distance 1 radius at the vertex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::GetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetDistance.md)
