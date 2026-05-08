# SetPartialEdgeFilletData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetPartialEdgeFilletData`

Sets the partial edge fillet data for the specified edge.
Sets the partial edge fillet data for the specified edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPartialEdgeFilletData( _
   ByVal FilletItem As System.Object, _
   ByVal PartialEdgeFilletData As System.Object _
) As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim FilletItem As System.Object
Dim PartialEdgeFilletData As System.Object
Dim value As System.Boolean
 
value = instance.SetPartialEdgeFilletData(FilletItem, PartialEdgeFilletData)
```

```

System.bool SetPartialEdgeFilletData( 
   System.object FilletItem,
   System.object PartialEdgeFilletData
)
```

```

System.bool SetPartialEdgeFilletData( 
   System.Object^ FilletItem,
   System.Object^ PartialEdgeFilletData
) 
```

#### Parameters

*FilletItem*
:   [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*PartialEdgeFilletData*
:   [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md); null to remove existing partial edge fillet data from FilletItem

#### Return Value

True if partial edge fillet data successfully set, false if not

Remarks

This method is valid only if [ISimpleFilletFeatureData2::EnablePartialEdgeParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetPartialEdgeFilletData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetPartialEdgeFilletData.md)
