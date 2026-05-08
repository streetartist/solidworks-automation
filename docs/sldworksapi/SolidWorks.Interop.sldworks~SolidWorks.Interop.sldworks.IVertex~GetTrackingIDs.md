# GetTrackingIDs Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs`

Gets the tracking IDs assigned to this vertex.
Gets the [tracking IDs assigned to this vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTrackingIDs( _
   ByVal TrackingCookie As System.Integer, _
   ByRef TrackingIDs As System.Object _
) As System.Integer
```

```

Dim instance As IVertex
Dim TrackingCookie As System.Integer
Dim TrackingIDs As System.Object
Dim value As System.Integer
 
value = instance.GetTrackingIDs(TrackingCookie, TrackingIDs)
```

```

System.int GetTrackingIDs( 
   System.int TrackingCookie,
   out System.object TrackingIDs
)
```

```

System.int GetTrackingIDs( 
   System.int TrackingCookie,
   [Out] System.Object^ TrackingIDs
) 
```

#### Parameters

*TrackingCookie*
:   Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.md)

*TrackingIDs*
:   Array of tracking IDs on this vertex

#### Return Value

Status as defined by [swTrackingIDError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

Remarks

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Example

[Get, Set, and Remove Tracking IDs on Vertex (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.md)  
[IVertex::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.md)  
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.md)  
[IVertex::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.md)  
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.md)
