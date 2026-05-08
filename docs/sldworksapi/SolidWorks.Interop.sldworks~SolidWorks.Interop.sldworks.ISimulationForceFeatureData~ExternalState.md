# ExternalState Property (ISimulationForceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ExternalState`

Gets or sets whether your application can listen to force-related motion study events.
Gets or sets whether your application can listen to force-related motion study events.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExternalState As System.Boolean
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Boolean
 
instance.ExternalState = value
 
value = instance.ExternalState
```

```

System.bool ExternalState {get; set;}
```

```

property System.bool ExternalState {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to listen to [IMotionStudy](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy.md) [ForceTimeStepChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler.md) and [ForceOutputTimeStampChangeNotify](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler.md) events, false to not

Remarks

When a force is set to external, IMotionStudy ForceTimeStepChangeNotify and ForceOutputTimeStampChangeNotify events are called with the motor name, time, and a pointer for the return value. These events are called at every major time step from ADAMS. You can implement any force law after catching these events. The return value for each event is a double that specifies the new force or torque magnitude.

Example

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)  
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)  
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)
