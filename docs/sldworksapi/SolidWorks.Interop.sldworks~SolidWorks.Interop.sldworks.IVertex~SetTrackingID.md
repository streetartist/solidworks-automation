# SetTrackingID Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID`

Assigns a tracking ID to this vertex.
Assigns a tracking ID to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTrackingID( _
   ByVal TrackingCookie As System.Integer, _
   ByVal TrackingID As System.Integer _
) As System.Integer
```

```

Dim instance As IVertex
Dim TrackingCookie As System.Integer
Dim TrackingID As System.Integer
Dim value As System.Integer
 
value = instance.SetTrackingID(TrackingCookie, TrackingID)
```

```

System.int SetTrackingID( 
   System.int TrackingCookie,
   System.int TrackingID
)
```

```

System.int SetTrackingID( 
   System.int TrackingCookie,
   System.int TrackingID
) 
```

#### Parameters

*TrackingCookie*
:   :   Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.md)

*TrackingID*
:   Application-defined value for the tracking ID

    |  |  |
    | --- | --- |
    | **Value** | **Action** |
    | >0 | Vertex is tracked |
    | 0 | Tracking of vertex is stopped |

#### Return Value

Status as defined by [swTrackingIDError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

Remarks

You can assign tracking IDs to [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md), and vertices in parts and assemblies only; you cannot assign tracking IDs to these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Example

[Get, Set, and Remove Tracking IDs on Vertex (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.md)  
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.md)  
[IVertex::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.md)  
[IVertex::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.md)  
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.md)
