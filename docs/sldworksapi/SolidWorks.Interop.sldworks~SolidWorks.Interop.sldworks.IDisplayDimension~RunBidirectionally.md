# RunBidirectionally Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally`

Gets or sets whether each dimension runs in a direction closest to the baseline in this angular running dimension.
Gets or sets whether each dimension runs in a direction closest to the baseline in this angular running dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RunBidirectionally As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.RunBidirectionally = value
 
value = instance.RunBidirectionally
```

```

System.bool RunBidirectionally {get; set;}
```

```

property System.bool RunBidirectionally {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if each dimension runs in a direction closest to the baseline, false if all dimensions run in the same direction (see **Remarks**)

Remarks

| If this property is... | Then... |
| --- | --- |
| True | No angle dimension in the angular running dimension is greater than 180⁰ from the baseline, and each angle is measured from a direction that is closest to the baseline. |
| False | The running direction of all angle dimensions is determined by the first angle dimension added. For example, if the user places the baseline dimension at the top of the part, clicking on a feature to the right of the baseline dimension forces all subsequent angular dimensions to be measured clockwise from the baseline. |

This property corresponds to the **Run bidirectionally** check box in the **Witness/Leader Display** panel of the **Leaders** tab of the **Dimension** PropertyManager page that appears when you right-click in a drawing and select **More Dimensions > Angular Running Dimension**.

Example

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)  
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)  
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.md)  
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.md)  
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)
