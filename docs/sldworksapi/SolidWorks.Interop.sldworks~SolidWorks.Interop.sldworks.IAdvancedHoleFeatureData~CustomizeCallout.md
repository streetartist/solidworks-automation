# CustomizeCallout Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~CustomizeCallout`

Gets or sets whether to customize the hole callouts of the elements of this Advanced Hole.
Gets or sets whether to customize the hole callouts of the elements of this Advanced Hole.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomizeCallout As System.Boolean
```

```

Dim instance As IAdvancedHoleFeatureData
Dim value As System.Boolean
 
instance.CustomizeCallout = value
 
value = instance.CustomizeCallout
```

```

System.bool CustomizeCallout {get; set;}
```

```

property System.bool CustomizeCallout {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to customize hole callouts, false to use default hole callouts

Remarks

If you set this property to true, use [IAdvancedHoleElementData::CalloutString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.md) to customize the hole callouts.

Example

See the [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md)  
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.md)
