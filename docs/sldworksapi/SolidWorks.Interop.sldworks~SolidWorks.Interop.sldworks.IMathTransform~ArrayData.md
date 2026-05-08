# ArrayData Property (IMathTransform)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ArrayData`

Gets and sets the array of 16 doubles for this transform.
Gets and sets the array of 16 doubles for this transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ArrayData As System.Object
```

```

Dim instance As IMathTransform
Dim value As System.Object
 
instance.ArrayData = value
 
value = instance.ArrayData
```

```

System.object ArrayData {get; set;}
```

```

property System.Object^ ArrayData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of 16 doubles (see **Remarks**)

Remarks

The first 9 elements define the 3x3 rotation matrix. The next 3 elements define the translation component. The next element defines the scaling component. The last 3 elements are unused.

The array data argument should be in a form that allows the direct calling of methods such as [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md).

Example

[Get Angle Between Plane and Line (VBA)](Get_Angle_Between_Plane_and_Line_Example_VB.htm)  
[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)  
[Get Transform of Plane (VBA)](Get_Transform_of_Plane_Example_VB.htm)  
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)  
[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[IMathTransform::IArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IArrayData.md)
