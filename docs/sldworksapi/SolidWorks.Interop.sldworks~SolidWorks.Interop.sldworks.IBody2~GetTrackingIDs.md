# GetTrackingIDs Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs`

Gets the tracking IDs assigned to this body.
Gets the [tracking IDs assigned to this body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md).

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

Dim instance As IBody2
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
:   :   Array of tracking IDs on this body

#### Return Value

Status as defined by [swTrackingIDError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

Remarks

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

Example

[Get, Set, and Remove Tracking IDs on Body (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.md)  
[IBody2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.md)  
[IBody2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.md)  
[IBody2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md)  
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.md)
