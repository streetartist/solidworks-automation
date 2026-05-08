# GetDistance Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetDistance`

Gets the Distance 2 radius for this asymmetric fillet.
Gets the Distance 2 radius for this asymmetric fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDistance( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double
 
value = instance.GetDistance(PFilletItem)
```

```

System.double GetDistance( 
   System.object PFilletItem
)
```

```

System.double GetDistance( 
   System.Object^ PFilletItem
) 
```

#### Parameters

*PFilletItem*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) at which to get the radius

#### Return Value

Distance 2 radius at the vertex for the asymmetric fillet

Remarks

Call [IVariableFilletFeatureData2::GetRadius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md) to get the Distance 1 radius at the vertex for this asymmetric fillet.

Example

See the [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::SetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetDistance.md)
