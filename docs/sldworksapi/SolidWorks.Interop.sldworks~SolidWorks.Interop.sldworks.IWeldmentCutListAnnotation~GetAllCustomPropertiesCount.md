# GetAllCustomPropertiesCount Method (IWeldmentCutListAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomPropertiesCount`

Gets the number of items in the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.
Gets the number of items in the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllCustomPropertiesCount() As System.Integer
```

```

Dim instance As IWeldmentCutListAnnotation
Dim value As System.Integer
 
value = instance.GetAllCustomPropertiesCount()
```

```

System.int GetAllCustomPropertiesCount()
```

```

System.int GetAllCustomPropertiesCount(); 
```

#### Return Value

Number of available custom properties

Remarks

Call this method before calling [IWeldmentCutListAnnotation::IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties.md).

The list of possible custom properties includes all of the items in the weldment cut list table, which includes items from the file summary items and file custom properties that have been set.

Example

[Get Weldment Cut List Feature and Annotations (VBA)](Get_Weldment_Cut-list_Feature_and_Annotations_Example_VB.htm)  
[Get Weldment Cut List Feature and Annotations (VB.NET)](Get_Weldment_Cut-list_Feature_and_Annotations_Example_VBNET.htm)  
[Get Weldment Cut List Feature and Annotations (C#)](Get_Weldment_Cut-list_Feature_and_Annotations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)  
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.md)  
[IWeldmentCutListAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.md)  
[IWeldmentCutListAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty.md)  
[IWeldmentCutListAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty.md)
