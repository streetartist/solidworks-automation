# CalloutString Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString`

Gets or sets the hole callout string for this Advanced Hole element.
Gets or sets the hole callout string for this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CalloutString As System.String
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.String
 
instance.CalloutString = value
 
value = instance.CalloutString
```

```

System.string CalloutString {get; set;}
```

```

property System.String^ CalloutString {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Hole callout string (see **Remarks**)

Remarks

This property is valid only if [IAdvancedHoleFeatureData::CustomizeCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~CustomizeCallout.md) is set to true.

The hole callout string is formatted as follows:

<*LibraryName*-*SymbolName*> <*callout\_var1*> <*callout\_var2*>... <*callout\_varn*>

where:

- *LibraryName* and *SymbolName* are defined in ***c:\ProgramData\SolidWorks\SolidWorks 20**nn**\lang\english\gtol.sym**.*
- *callout\_var1-n* are callout variables. Use [IModelDocExtension::GetCalloutVariableString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCalloutVariableString.md) to get the strings for hole callout variables defined in [swCalloutVariable\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariable_e.html). You can also find the hole callout variable strings by clicking **Hole Callout > Callout Variables** in the Advanced Hole PropertyManager.

**Note**: You must include the right- and left-angle brackets and the hyphens when setting the elements of this property string:

```

   "<HOLE-SPOT><MOD-DIAM> <ah-cboredia> <HOLE-DEPTH> <ah-cboredepth><ah-cboreside>"
```

Example

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)
