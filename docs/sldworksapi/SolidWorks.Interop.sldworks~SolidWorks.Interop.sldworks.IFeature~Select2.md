# Select2 Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2`

Selects and marks this feature.
Selects and marks this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeature
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean
 
value = instance.Select2(Append, Mark)
```

```

System.bool Select2( 
   System.bool Append,
   System.int Mark
)
```

```

System.bool Select2( 
   System.bool Append,
   System.int Mark
) 
```

#### Parameters

*Append*
:   True appends the feature to the current selection list, false replaces the current selection list

*Mark*
:   Value you want to use as a mark; this number is used by functions that require ordered selection

#### Return Value

True if the feature was selected, false if not

Remarks

If an object is already selected with a mark of *x* and you attempt to select the same object again using this method with Append = true and Mark = *y*, then that object remains selected with a mark with *x*. Reselecting a previously selected object does not assign a new mark value.

Example

[Get Plane or Face for Sketch (VBA)](Get_Plane_or_Face_for_Sketch_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Traverse Assembly and Hide All Sketches (VBA)](Traverse_Assembly_and_Hide_All_Sketches_Example_VB.htm)  
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)  
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)  
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)  
[Select Plane (VBA)](Select_Plane_Example_VB.htm)  
[Select Plane (VB.NET)](Select_Plane_Example_VBNET.htm)  
[Select Plane (C#)](Select_Plane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DeSelect.md)  
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md)
