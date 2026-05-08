# ISetComponentState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentState`

Sets the suppression state for the specified components.
Sets the suppression state for the specified components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetComponentState( _
   ByVal SuppressionState As System.Integer, _
   ByVal NumComps As System.Integer, _
   ByRef CompArr As Component2, _
   ByVal ConfigOption As System.Integer, _
   ByVal WhichConfig As System.String, _
   ByVal SaveClosedDocs As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim SuppressionState As System.Integer
Dim NumComps As System.Integer
Dim CompArr As Component2
Dim ConfigOption As System.Integer
Dim WhichConfig As System.String
Dim SaveClosedDocs As System.Boolean
Dim value As System.Boolean
 
value = instance.ISetComponentState(SuppressionState, NumComps, CompArr, ConfigOption, WhichConfig, SaveClosedDocs)
```

```

System.bool ISetComponentState( 
   System.int SuppressionState,
   System.int NumComps,
   ref Component2 CompArr,
   System.int ConfigOption,
   System.string WhichConfig,
   System.bool SaveClosedDocs
)
```

```

System.bool ISetComponentState( 
   System.int SuppressionState,
   System.int NumComps,
   Component2^% CompArr,
   System.int ConfigOption,
   System.String^ WhichConfig,
   System.bool SaveClosedDocs
) 
```

#### Parameters

*SuppressionState*
:   Component suppression state as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html) (see **Remarks**)

*NumComps*
:   Number of components to change

*CompArr*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to change of size numComps

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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.md)
