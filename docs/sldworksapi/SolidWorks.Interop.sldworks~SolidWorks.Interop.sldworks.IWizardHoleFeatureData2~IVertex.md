# IVertex Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IVertex`

Gets the end-condition vertex for the Hole Wizard feature.
Gets the end-condition vertex for the Hole Wizard feature.

****NOTE:** This property is a get-only property. Set is not implemented.**

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IVertex As Vertex
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As Vertex
 
instance.IVertex = value
 
value = instance.IVertex
```

```

Vertex IVertex {get; set;}
```

```

property Vertex^ IVertex {
   Vertex^ get();
   void set (    Vertex^ value);
}
```

#### Property Value

[Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

To if end condition is to a vertex, use [IWizardHoleFeatureData2::SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~SetEndConditionReference.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Vertex.md)  
[IWizardHoleFeatureData2::EndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~EndCondition.md)  
[IWizardHoleFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetEndConditionReference.md)
