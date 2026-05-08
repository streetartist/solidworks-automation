# SetTrackingID Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID`

Assigns a tracking ID to this body.
Assigns a tracking ID to this body.

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

Dim instance As IBody2
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
:   Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.md)

*TrackingID*
:   Application-defined value for the tracking ID

    |  |  |
    | --- | --- |
    | **Value** | **Action** |
    | >0 | Body is tracked |
    | 0 | Tracking of body is stopped |

#### Return Value

Status as defined by [swTrackingIDError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

Remarks

You can assign tracking IDs to bodies, [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md), and [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) in parts and assemblies only; you cannot assign tracking IDs to these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Example

[Get, Set, and Remove Tracking IDs on Body (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.md)  
[IBody2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.md)  
[IBody2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.md)  
[IBody2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.md)  
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.md)
