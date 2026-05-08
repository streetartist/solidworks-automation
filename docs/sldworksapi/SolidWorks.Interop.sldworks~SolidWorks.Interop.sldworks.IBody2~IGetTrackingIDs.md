# IGetTrackingIDs Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs`

Gets the tracking IDs assigned to this body.
Gets the [tracking IDs assigned to this body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md).

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

Dim instance As IBody2
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
:   :   Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.md)

*Count*
:   Number of tracking IDs

*TrackingIDs*
:   - in-process, unmanaged C++: Pointer to an array of tracking IDs on this body

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Status as defined by [swTrackingIDError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

Remarks

Before calling this method, call [IBody2::GetTrackingIDsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.md) to determine Count.

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.md)  
[IBody2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.md)  
[IBody2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md)  
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.md)
