# FindTrackedObjects Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects`

Finds the tracking IDs assigned to entities in this document.
Finds the tracking IDs assigned to entities in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindTrackedObjects( _
   ByVal TrackingCookie As System.Integer, _
   ByVal SearchObject As System.Object, _
   ByVal TypesFilter As System.Object, _
   ByVal TrackingIDs As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim TrackingCookie As System.Integer
Dim SearchObject As System.Object
Dim TypesFilter As System.Object
Dim TrackingIDs As System.Object
Dim value As System.Object
 
value = instance.FindTrackedObjects(TrackingCookie, SearchObject, TypesFilter, TrackingIDs)
```

```

System.object FindTrackedObjects( 
   System.int TrackingCookie,
   System.object SearchObject,
   System.object TypesFilter,
   System.object TrackingIDs
)
```

```

System.Object^ FindTrackedObjects( 
   System.int TrackingCookie,
   System.Object^ SearchObject,
   System.Object^ TypesFilter,
   System.Object^ TrackingIDs
) 
```

#### Parameters

*TrackingCookie*
:   Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.md)

*SearchObject*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) or [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to search for tracking IDs; if empty, then all bodies in the document are searched

*TypesFilter*
:   Array of the type of entities for which to search as defined by [swTopoEntity\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTopoEntity_e.html); valid values are swTopoVertex, swTopoEdge, swTopoLoop, swTopoFace, and swTopoBody; if empty or set to 0, then all types are searched

*TrackingIDs*
:   Array of tracking IDs for which to search; if empty, then search for all tracking IDs

#### Return Value

Array of objects found that match the specified tracking cookie, types, and tracking IDs; this list can be empty if no matches are found

Remarks

You can set tracking IDs on [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md), and [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) in parts and assemblies only; you cannot set tracking IDs on these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IBody2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.md)  
[IBody2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.md)  
[IBody2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.md)  
[IBody2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md)  
[IEdge::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.md)  
[IEdge::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.md)  
[IEdge::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.md)  
[IEdge::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.md)  
[IFace2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDs.md)  
[IFace2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDsCount.md)  
[IFace2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTrackingID.md)  
[IFace2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.md)  
[ILoop2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDs.md)  
[ILoop2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDsCount.md)  
[ILoop2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RemoveTrackingID.md)  
[ILoop2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SetTrackingID.md)  
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.md)  
[IVertex::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.md)  
[IVertex::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.md)  
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.md)  
[IVertex::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.md)  
[ILoop2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetTrackingIDs.md)  
[IFace2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrackingIDs.md)  
[IEdge::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.md)  
[IBody2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.md)
