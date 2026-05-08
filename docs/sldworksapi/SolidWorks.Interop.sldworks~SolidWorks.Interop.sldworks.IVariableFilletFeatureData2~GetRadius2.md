# GetRadius2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2`

Gets the value of the Distance 1 radius at the specified vertex.
Gets the value of the Distance 1 radius at the specified vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRadius2( _
   ByVal PFilletItem As Vertex, _
   ByRef IsAssigned As System.Boolean _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim IsAssigned As System.Boolean
Dim value As System.Double
 
value = instance.GetRadius2(PFilletItem, IsAssigned)
```

```

System.double GetRadius2( 
   Vertex PFilletItem,
   out System.bool IsAssigned
)
```

```

System.double GetRadius2( 
   Vertex^ PFilletItem,
   [Out] System.bool IsAssigned
) 
```

#### Parameters

*PFilletItem*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) at which to get the radius

*IsAssigned*
:   True if the radius is assigned to a control point, false if not

#### Return Value

Fillet radius at the vertex specified by PFilletItem for the symmetric fillet; Distance 1 radius at the vertex for the asymmetric fillet (see **Remarks**)

Remarks

Call [IVariableFilletFeatureData2::GetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetDistance.md) to get the Distance 2 radius at the vertex for the asymmetric fillet.

Example

See the [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.md)  
[IVariableFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.md)  
[IVariableFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.md)  
[IVariableFilletFeatureData2::GetConicRhoOrRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.md)
