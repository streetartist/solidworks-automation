# SetComponentState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState`

Sets the suppression state for the specified components.
Sets the suppression state for the specified components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponentState( _
   ByVal SuppressionState As System.Integer, _
   ByVal CompArr As System.Object, _
   ByVal ConfigOption As System.Integer, _
   ByVal WhichConfig As System.String, _
   ByVal SaveClosedDocs As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim SuppressionState As System.Integer
Dim CompArr As System.Object
Dim ConfigOption As System.Integer
Dim WhichConfig As System.String
Dim SaveClosedDocs As System.Boolean
Dim value As System.Boolean
 
value = instance.SetComponentState(SuppressionState, CompArr, ConfigOption, WhichConfig, SaveClosedDocs)
```

```

System.bool SetComponentState( 
   System.int SuppressionState,
   System.object CompArr,
   System.int ConfigOption,
   System.string WhichConfig,
   System.bool SaveClosedDocs
)
```

```

System.bool SetComponentState( 
   System.int SuppressionState,
   System.Object^ CompArr,
   System.int ConfigOption,
   System.String^ WhichConfig,
   System.bool SaveClosedDocs
) 
```

#### Parameters

*SuppressionState*
:   Component suppression state as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html) (see **Remarks**)

*CompArr*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to change

*ConfigOption*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*WhichConfig*
:   Name of the configuration to change

*SaveClosedDocs*
:   True saves closed documents, false does not

#### Return Value

True if the components were changed, false if not

Remarks

You cannot set a component to lightweight using this method. Instead, use [IComponent::SetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md).

Example

[Set Component State (VBA)](Set_Component_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.md)
