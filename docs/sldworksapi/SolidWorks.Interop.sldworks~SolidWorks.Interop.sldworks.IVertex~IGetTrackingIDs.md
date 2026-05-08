# IGetTrackingIDs Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs`

Gets the tracking IDs assigned to this vertex.
Gets the [tracking IDs assigned to this vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTrackingIDs( _
   ByVal TrackingCookie As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef TrackingIDs As System.Integer _
) As System.Integer
```

```

Dim instance As IVertex
Dim TrackingCookie As System.Integer
Dim Count As System.Integer
Dim TrackingIDs As System.Integer
Dim value As System.Integer
 
value = instance.IGetTrackingIDs(TrackingCookie, Count, TrackingIDs)
```

```

System.int IGetTrackingIDs( 
   System.int TrackingCookie,
   System.int Count,
   out System.int TrackingIDs
)
```

```

System.int IGetTrackingIDs( 
   System.int TrackingCookie,
   System.int Count,
   [Out] System.int TrackingIDs
) 
```

#### Parameters

*TrackingCookie*
:   Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.md)

*Count*
:   Number of tracking IDs on this vertex

*TrackingIDs*
:   - in-process, unmanaged C++: Pointer to an array of tracking IDs on this vertex

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Status as defined by [swTrackingIDError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

Remarks

Before calling this method, call [IVertex::GetTrackingIDsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.md) to get Count.

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.md)  
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.md)  
[IVertex::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.md)  
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.md)
