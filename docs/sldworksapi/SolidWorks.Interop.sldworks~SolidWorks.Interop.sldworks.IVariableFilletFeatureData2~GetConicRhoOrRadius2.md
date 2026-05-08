# GetConicRhoOrRadius2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2`

Gets the conic rho or radius at the specified vertex.
Gets the conic rho or radius at the specified vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConicRhoOrRadius2( _
   ByVal PFilletItem As Vertex, _
   ByRef IsAssigned As System.Boolean _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim IsAssigned As System.Boolean
Dim value As System.Double
 
value = instance.GetConicRhoOrRadius2(PFilletItem, IsAssigned)
```

```

System.double GetConicRhoOrRadius2( 
   Vertex PFilletItem,
   out System.bool IsAssigned
)
```

```

System.double GetConicRhoOrRadius2( 
   Vertex^ PFilletItem,
   [Out] System.bool IsAssigned
) 
```

#### Parameters

*PFilletItem*
:   Vertex for which to get a value (see **Remarks**)

*IsAssigned*
:   True if the conic value is assigned to each control point, false if not

#### Return Value

Conic rho or radius

Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetFilletEdgeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.md) to specify PFilletItem.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) is set to [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then this method returns a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then this method returns a conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::GetRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md)
