# GetPartialEdgeFilletData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetPartialEdgeFilletData`

Gets the partial edge fillet data for the specified edge.
Gets the partial edge fillet data for the specified edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPartialEdgeFilletData( _
   ByVal FilletItem As System.Object _
) As System.Object
```

```

Dim instance As ISimpleFilletFeatureData2
Dim FilletItem As System.Object
Dim value As System.Object
 
value = instance.GetPartialEdgeFilletData(FilletItem)
```

```

System.object GetPartialEdgeFilletData( 
   System.object FilletItem
)
```

```

System.Object^ GetPartialEdgeFilletData( 
   System.Object^ FilletItem
) 
```

#### Parameters

*FilletItem*
:   [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

[IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md); null if FilletItem is not an edge

Remarks

This method is valid only if [ISimpleFilletFeatureData2::EnablePartialEdgeParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.md) is true.

Example

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::SetPartialEdgeFilletData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetPartialEdgeFilletData.md)
